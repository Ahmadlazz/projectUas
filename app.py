import streamlit as st
import networkx as nx
import pandas as pd
import folium
import math
import heapq
import requests  
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium

# 1. KONFIGURASI HALAMAN
st.set_page_config(
    page_title="DSS Rute Kurir - Struktur Data UAS",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Kustomisasi Tema Premium Tanpa Emoji (Menggunakan Desain UI Modern)
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    .main-title {
        font-size: 2.4rem;
        font-weight: 800;
        color: #5d2431;
        letter-spacing: -0.03em;
        margin-bottom: 0.15rem;
    }
    .subtitle {
        color: #6f6570;
        font-size: 1rem;
        font-weight: 500;
        margin-bottom: 1.5rem;
    }
    .card {
        background: #ffffff;
        border: 1px solid rgba(124, 66, 81, 0.15);
        border-radius: 14px;
        padding: 1.3rem;
        box-shadow: 0 4px 20px rgba(92, 42, 56, 0.03);
        margin-bottom: 1rem;
    }
    .result-card {
        background: linear-gradient(135deg, #7C4251 0%, #5f2f3b 100%);
        color: white;
        border-radius: 14px;
        padding: 1.5rem;
        box-shadow: 0 10px 30px rgba(124, 66, 81, 0.2);
        margin-bottom: 1.5rem;
    }
    .path-badge {
        display: inline-block;
        background: rgba(255,255,255,0.15);
        color: white;
        padding: 0.4rem 0.8rem;
        border-radius: 8px;
        margin-right: 0.4rem;
        margin-bottom: 0.4rem;
        font-weight: 600;
        font-size: 0.9rem;
        border: 1px solid rgba(255,255,255,0.1);
    }
    [data-testid="stSidebar"] {
        background: #fbf8f9;
        border-right: 1px solid rgba(124, 66, 81, 0.08);
    }
    .stButton > button {
        border-radius: 10px;
        border: 0;
        background: #7C4251;
        color: white;
        font-weight: 600;
        padding: 0.6rem 1rem;
        width: 100%;
        transition: all 0.2s;
    }
    .stButton > button:hover {
        background: #65323f;
        box-shadow: 0 4px 12px rgba(124, 66, 81, 0.25);
    }
    div[data-testid="stMetric"] {
        background: white;
        border: 1px solid rgba(124, 66, 81, 0.1);
        padding: 1.2rem;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(92, 42, 56, 0.02);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 2. STRUKTUR DATA GRAPH (ADJACENCY LIST)
class CourierDSSGraph:
    def __init__(self):
        self.adjacency_list = {}

    def add_node(self, node):
        if node not in self.adjacency_list:
            self.adjacency_list[node] = []

    def add_edge(self, u, v, weight, bidirectional=True):
        self.add_node(u)
        self.add_node(v)
        if (v, weight) not in self.adjacency_list[u]:
            self.adjacency_list[u].append((v, weight))
        if bidirectional and (u, weight) not in self.adjacency_list[v]:
            self.adjacency_list[v].append((u, weight))

    def dijkstra_process(self, start, target):
        if start not in self.adjacency_list or target not in self.adjacency_list:
            return [], float("inf"), []

        distances = {node: float("inf") for node in self.adjacency_list}
        distances[start] = 0
        previous = {node: None for node in self.adjacency_list}
        pq = [(0, start)] 
        visited = set()
        logs = []

        while pq:
            current_distance, current_node = heapq.heappop(pq)
            if current_node in visited:
                continue
            visited.add(current_node)

            logs.append({
                "Langkah": len(logs) + 1,
                "Node": current_node,
                "Jarak": f"{current_distance} km",
                "Proses": f"Node '{current_node}' diekstrak dari antrean prioritas."
            })

            if current_node == target:
                break

            for neighbor, weight in self.adjacency_list[current_node]:
                new_distance = current_distance + weight
                if new_distance < distances[neighbor]:
                    old_dist = distances[neighbor]
                    distances[neighbor] = new_distance
                    previous[neighbor] = current_node
                    heapq.heappush(pq, (new_distance, neighbor))
                    
                    old_str = "∞" if old_dist == float('inf') else f"{old_dist} km"
                    logs.append({
                        "Langkah": len(logs) + 1,
                        "Node": neighbor,
                        "Jarak": f"{new_distance} km",
                        "Proses": f"Relaksasi edge ({current_node} -> {neighbor}). Jarak diperbarui dari {old_str} menjadi {new_distance} km."
                    })

        if distances[target] == float("inf"):
            return [], float("inf"), logs

        path = []
        cur = target
        while cur is not None:
            path.insert(0, cur)
            cur = previous[cur]

        return path, round(distances[target], 2), logs

# 3. FUNGSI UTILITAS & API ROUTING
def haversine_distance(coord1, coord2):
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return round(6371.0 * c, 2)

def get_osrm_route(coords_list):
    if len(coords_list) < 2:
        return coords_list
    loc_string = ";".join([f"{lon},{lat}" for lat, lon in coords_list])
    url = f"http://router.project-osrm.org/route/v1/driving/{loc_string}?overview=full&geometries=geojson"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            if data.get("routes") and len(data["routes"]) > 0:
                geometry = data["routes"][0]["geometry"]["coordinates"]
                return [[lat, lon] for lon, lat in geometry]
    except Exception:
        pass
    return coords_list

def build_osm_graph(coords_dict):
    G_osm = nx.Graph()
    for node_name, (lat, lon) in coords_dict.items():
        G_osm.add_node(node_name, y=lat, x=lon)
    return G_osm

def build_map(G, route_nodes=None, origin_node=None, destination_node=None):
    route_nodes = route_nodes or []
    if origin_node is not None and origin_node in G.nodes:
        origin_point = (G.nodes[origin_node]["y"], G.nodes[origin_node]["x"])
    else:
        origin_point = (-8.6705, 115.2126)

    m = folium.Map(location=origin_point, zoom_start=13, tiles="OpenStreetMap", control_scale=True)
    cluster = MarkerCluster(name="Jaringan Distribusi").add_to(m)

    for node, data in G.nodes(data=True):
        lat, lon = data["y"], data["x"]
        if node == origin_node:
            color, icon = "green", "play"
        elif node == destination_node:
            color, icon = "red", "flag"
        else:
            color, icon = "cadetblue", "info-sign"

        folium.Marker(
            location=[lat, lon],
            tooltip=str(node),
            popup=folium.Popup(f"<b>{node}</b><br>Lat: {lat}<br>Lon: {lon}", max_width=220),
            icon=folium.Icon(color=color, icon=icon)
        ).add_to(cluster)

    if route_nodes and len(route_nodes) >= 2:
        full_road_geometry = []
        with st.spinner("Menyelaraskan rute dengan jaringan jalan raya Bali..."):
            for i in range(len(route_nodes) - 1):
                node_asal = route_nodes[i]
                node_tujuan = route_nodes[i+1]
                if node_asal in G.nodes and node_tujuan in G.nodes:
                    coord_asal = (G.nodes[node_asal]["y"], G.nodes[node_asal]["x"])
                    coord_tujuan = (G.nodes[node_tujuan]["y"], G.nodes[node_tujuan]["x"])
                    segment_geometry = get_osrm_route([coord_asal, coord_tujuan])
                    full_road_geometry.extend(segment_geometry)

        if full_road_geometry:
            folium.PolyLine(
                locations=full_road_geometry,
                color="#d62828",
                weight=6,
                opacity=0.85,
            ).add_to(m)
            m.fit_bounds(full_road_geometry)

    legend_html = """
    <div style="position: fixed; bottom: 30px; left: 30px; z-index: 9999; background: white; padding: 12px 14px; 
    border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); font-size: 11px; color: #333; font-family: sans-serif;">
        <b style="color:#7C4251; display:block; margin-bottom:4px;">Legenda Navigasi</b>
        <span style="color:green;">●</span> Titik Keberangkatan<br>
        <span style="color:red;">●</span> Titik Penerima<br>
        <span style="color:cadetblue;">●</span> Hub Alternatif<br>
        <span style="color:#d62828;">▬</span> Rute Optimal (Jalan Raya)
    </div>
    """
    m.get_root().html.add_child(folium.Element(legend_html))
    return m

# 4. INISIALISASI STATE DATA
if "coords" not in st.session_state:
    st.session_state["coords"] = {
        "Kantor Pusat": (-8.6705, 115.2126),
        "Hub Denpasar": (-8.6541, 115.2160),
        "Hub Kuta": (-8.7233, 115.1720),
        "Penerima A": (-8.6400, 115.2220),
        "Penerima B": (-8.6900, 115.1850),
        "Penerima C": (-8.7100, 115.2050),
    }

if "graph_obj" not in st.session_state:
    g = CourierDSSGraph()
    default_edges = [
        ("Kantor Pusat", "Hub Denpasar", 5.2),
        ("Kantor Pusat", "Hub Kuta", 7.8),
        ("Hub Denpasar", "Penerima A", 4.1),
        ("Hub Denpasar", "Hub Kuta", 2.5),
        ("Hub Kuta", "Penerima B", 5.9),
        ("Penerima A", "Penerima B", 3.4),
        ("Penerima A", "Penerima C", 6.8),
        ("Penerima B", "Penerima C", 2.1)
    ]
    for u, v, w in default_edges:
        g.add_edge(u, v, w)
    st.session_state["graph_obj"] = g

g_obj = st.session_state["graph_obj"]
coords_data = st.session_state["coords"]

# 5. STRUKTUR INTERFACE UTAMA
st.markdown('<div class="main-title">Decision Support System Rute Kurir</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Optimasi Distribusi Logistik Berbasis Struktur Data Graph & Algoritma Dijkstra</div>', unsafe_allow_html=True)
st.markdown("---")

with st.sidebar:
    st.header("Analisis Rute")
    nodes_pilihan = list(g_obj.adjacency_list.keys())
    start = st.selectbox("Pilih Titik Awal (Start):", options=nodes_pilihan, index=0)
    end = st.selectbox("Pilih Titik Tujuan (End):", options=nodes_pilihan, index=1 if len(nodes_pilihan) > 1 else 0)
    
    # Ikon dipindahkan ke dalam teks string
    run_analysis = st.button(":material/navigation: Hitung Rute Optimal")

if run_analysis:
    path_hasil, dist_hasil, logs_hasil = g_obj.dijkstra_process(start, end)
    if dist_hasil == float("inf") or not path_hasil:
        st.sidebar.error("Rute Terputus! Periksa kembali relasi graph.")
        st.session_state["output_ready"] = False
    else:
        st.session_state["output_ready"] = True
        st.session_state["path_hasil"] = path_hasil
        st.session_state["dist_hasil"] = dist_hasil
        st.session_state["logs_hasil"] = logs_hasil
        st.session_state["start_aktif"] = start
        st.session_state["end_aktif"] = end

col_kiri, col_kanan = st.columns([1, 1.4], gap="medium")

with col_kiri:
    # Ikon dimasukkan langsung ke dalam teks judul
    st.subheader(":material/text_snippet: Matriks Ketetanggaan (Adjacency List)")
    tabel_edge = []
    seen_edges = set()
    for node_asal, tetangga_list in g_obj.adjacency_list.items():
        for node_tujuan, bobot in tetangga_list:
            identitas_unik_edge = tuple(sorted((node_asal, node_tujuan)))
            if identitas_unik_edge not in seen_edges:
                seen_edges.add(identitas_unik_edge)
                tabel_edge.append({"Dari Node": node_asal, "Ke Node": node_tujuan, "Jarak Relatif": f"{bobot} km"})
                
    st.write(f"**Total Node:** {len(g_obj.adjacency_list)} | **Total Edges:** {len(tabel_edge)}")
    st.dataframe(pd.DataFrame(tabel_edge), use_container_width=True, hide_index=True)

with col_kanan:
    # Ikon dimasukkan langsung ke dalam teks judul
    st.subheader(":material/map: Visualisasi Spasial")
    st.caption("Klik pada area peta untuk menangkap koordinat lokasi secara otomatis.")
    
    osm_graph_data = build_osm_graph(coords_data)
    
    ready = st.session_state.get("output_ready", False)
    path_map = st.session_state.get("path_hasil", []) if ready else None
    s_map = st.session_state.get("start_aktif", None) if ready else None
    e_map = st.session_state.get("end_aktif", None) if ready else None
    
    peta_folium = build_map(osm_graph_data, route_nodes=path_map, origin_node=s_map, destination_node=e_map)
    
    folium.LatLngPopup().add_to(peta_folium)
    map_data = st_folium(peta_folium, width="100%", height=450, key="dss_interactive_map")

    clicked_coords = None
    if map_data and map_data.get("last_clicked"):
        clicked_coords = (map_data["last_clicked"]["lat"], map_data["last_clicked"]["lng"])
        # Menggunakan st.info standar
        st.info(f"Koordinat Terpilih: Lat {clicked_coords[0]:.5f}, Lon {clicked_coords[1]:.5f}")

with st.sidebar:
    st.markdown("---")
    st.header("Kelola Node & Edge")
    
    default_lat = clicked_coords[0] if clicked_coords else -8.6700
    default_lon = clicked_coords[1] if clicked_coords else 115.2100
    
    with st.form("form_input_baru", clear_on_submit=True):
        nama_node_baru = st.text_input("Nama Lokasi Baru:", placeholder="Contoh: Hub Timur")
        lat_baru = st.number_input("Latitude:", value=default_lat, format="%.5f")
        lon_baru = st.number_input("Longitude:", value=default_lon, format="%.5f")
        
        node_tetangga = st.selectbox("Hubungkan langsung ke:", options=nodes_pilihan)
        # Ikon dipindahkan ke dalam teks string
        submit_btn = st.form_submit_button(":material/add_location_alt: Tambah Node & Relasi")
        
        if submit_btn and nama_node_baru:
            if nama_node_baru in coords_data:
                st.error("Lokasi sudah terdaftar!")
            else:
                titik_baru_coord = (lat_baru, lon_baru)
                titik_tetangga_coord = coords_data[node_tetangga]
                jarak_hitung = haversine_distance(titik_baru_coord, titik_tetangga_coord)
                
                st.session_state["coords"][nama_node_baru] = titik_baru_coord
                g_obj.add_edge(nama_node_baru, node_tetangga, jarak_hitung)
                st.rerun()

if st.session_state.get("output_ready", False):
    st.markdown("---")
    
    st.markdown(
        f"""
        <div class="result-card">
            <h4 style="margin:0 0 0.6rem 0; font-size:1.25rem; font-weight:700;">Rekomendasi Jalur Distribusi</h4>
            <div style="margin-bottom:0.4rem;">
                {" ".join([f'<span class="path-badge">{node}</span>' for node in st.session_state["path_hasil"]])}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Menghapus argumen icon pada st.metric karena versi lama belum mendukungnya
    m1, m2, m3 = st.columns(3)
    m1.metric("Total Jarak Tempuh", f"{st.session_state['dist_hasil']} Km")
    m2.metric("Titik Pemberhentian", f"{len(st.session_state['path_hasil'])} Node")
    m3.metric("Status Hasil", "Optimal")
    
    # Ikon dimasukkan langsung ke dalam teks judul
    st.subheader(":material/insights: Log Perhitungan Algoritma Dijkstra")
    df_logs = pd.DataFrame(st.session_state["logs_hasil"])
    st.dataframe(df_logs, use_container_width=True, hide_index=True)