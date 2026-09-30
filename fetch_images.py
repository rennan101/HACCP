import os
import requests
from PIL import Image
from io import BytesIO

# Freepik / Storyset (Rafiki Style) Explainer Illustrations matching Squideo aesthetic
STORYSET_URLS = {
    "slide_01.jpg": "https://stories.freepiklabs.com/storage/40405/online-learning-rafiki-5478.png", # Online food safety course introduction
    "slide_05.jpg": "https://stories.freepiklabs.com/storage/49024/biologist-rafiki-7649.png", # Biologist examining pathogens in lab
    "slide_09.jpg": "https://stories.freepiklabs.com/storage/13400/manufacturing-process-rafiki-2327.png", # Industrial processing tanks & machinery
    "slide_11.jpg": "https://stories.freepiklabs.com/storage/11648/temperature-measurement-rafiki-2700.png", # Temperature control & heat treatment
    "slide_12.jpg": "https://stories.freepiklabs.com/storage/16622/logistics-rafiki-2881.png", # Packaging conveyor & cold storage distribution
    "slide_13.jpg": "https://stories.freepiklabs.com/storage/12900/checklist-rafiki-1002.png", # Quality control checklist & audit inspection
    "slide_14.jpg": "https://stories.freepiklabs.com/storage/78185/cleaning-service-rafiki-11927.png", # Sanitiser spray bottles & disinfection
    "slide_15.jpg": "https://stories.freepiklabs.com/storage/13858/warning-rafiki-2365.png", # Physical safety warning & caution barrier
    "slide_17.jpg": "https://stories.freepiklabs.com/storage/64913/eating-healthy-food-rafiki-3344.png", # Dairy foods & culinary recipe preparation
    "slide_18.jpg": "https://stories.freepiklabs.com/storage/61737/do-not-enter-sign-rafiki-9898.png", # Prohibition sign for strict nut-free policy
    "slide_20.jpg": "https://stories.freepiklabs.com/storage/12489/healthy-habit-rafiki-1636.png", # Handwashing hygiene with soap & running water
    "slide_21.jpg": "https://stories.freepiklabs.com/storage/14933/taking-notes-rafiki-1877.png", # Color-coded stationery pens & zoning records
    "slide_23.jpg": "https://stories.freepiklabs.com/storage/13630/take-away-rafiki-3019.png", # Sealed meal prep storage containers
    "slide_25.jpg": "https://stories.freepiklabs.com/storage/34055/team-work-rafiki-3941.png", # Multidisciplinary HACCP team collaboration
}

os.makedirs("presentation/assets/images", exist_ok=True)
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"}

def fetch_and_format_illustrations():
    target_w, target_h = 1200, 800
    for filename, url in STORYSET_URLS.items():
        out_path = os.path.join("presentation/assets/images", filename)
        try:
            print(f"Fetching illustration for {filename}...")
            r = requests.get(url, headers=headers, timeout=20)
            if r.status_code == 200:
                raw_im = Image.open(BytesIO(r.content)).convert("RGBA")
                # Create a crisp canvas with soft modern background #F8FAFC
                canvas = Image.new("RGBA", (target_w, target_h), (248, 250, 252, 255))
                
                # Scale illustration to fit comfortably with breathing room (approx 720px height)
                scale = min((target_w - 80) / raw_im.width, (target_h - 60) / raw_im.height)
                new_w = int(raw_im.width * scale)
                new_h = int(raw_im.height * scale)
                resized_im = raw_im.resize((new_w, new_h), Image.Resampling.LANCZOS)
                
                # Center on canvas
                paste_x = (target_w - new_w) // 2
                paste_y = (target_h - new_h) // 2
                canvas.paste(resized_im, (paste_x, paste_y), mask=resized_im)
                
                # Save as clean high-quality JPEG
                final_im = canvas.convert("RGB")
                final_im.save(out_path, "JPEG", quality=92)
                print(f"  -> Successfully formatted {filename} ({final_im.size})")
            else:
                print(f"  -> Error fetching {filename}: HTTP {r.status_code}")
        except Exception as e:
            print(f"  -> Failed {filename}: {e}")

if __name__ == "__main__":
    fetch_and_format_illustrations()
