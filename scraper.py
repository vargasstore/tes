import requests
from bs4 import BeautifulSoup

def get_kuota_prices(url, margin_percentage=10):
    # Fungsi scraping untuk kuota Axis
    # Kode ini akan mirip dengan yang sudah ada, tetapi disesuaikan per kebutuhan.
    pass  # Ganti dengan implementasi scraper sebelumnya

def get_diamond_ml(url, margin_percentage=10):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        diamond_list = []
        
        # Contoh scraping untuk harga diamond ML (sesuaikan selector CSS-nya)
        items = soup.select(".card-body .item")  # Ganti sesuai dengan HTML situs
        for item in items:
            nama = item.select_one(".nama-diamond").text.strip()
            harga = item.select_one(".harga").text.strip()
            harga = int(harga.replace("Rp", "").replace(",", ""))  # Convert ke integer
            
            harga_untung = harga + (harga * margin_percentage / 100)
            
            diamond_list.append({
                "nama": nama,
                "harga_asli": harga,
                "harga_untung": int(harga_untung),
            })
        
        return diamond_list
    else:
        print("Gagal mengakses halaman ML")
        return []

def get_diamond_ff(url, margin_percentage=10):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        diamond_list = []
        
        # Contoh scraping untuk harga diamond FF (sesuaikan selector CSS-nya)
        items = soup.select(".card-body .item")  # Ganti sesuai dengan HTML situs
        for item in items:
            nama = item.select_one(".nama-diamond").text.strip()
            harga = item.select_one(".harga").text.strip()
            harga = int(harga.replace("Rp", "").replace(",", ""))
            
            harga_untung = harga + (harga * margin_percentage / 100)
            
            diamond_list.append({
                "nama": nama,
                "harga_asli": harga,
                "harga_untung": int(harga_untung),
            })
        
        return diamond_list
    else:
        print("Gagal mengakses halaman FF")
        return []