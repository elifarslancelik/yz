import subprocess
import requests
import os
from dotenv import load_dotenv

load_dotenv()
deepseek_api_key = os.getenv("DEEPSEEK_API_KEY")


def get_yz(prompt):
    headers = {
        "Authorization": f"Bearer {deepseek_api_key}",
        "Content-Type": "application/json"
    }
    
    system_prompt = """YALNIZCA Mac terminal komutları üret. Hiçbir açıklama, yorum veya ek bilgi yazma.
Örnekler:
-ls
-cd ~/Desktop
-mkdir yeni_klasör
Sadece istenen komutu döndür, başka HİÇBİR şey yazma."""

    data = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3,  # Daha deterministik çıktı için
        "max_tokens": 100
    }
    
    response = requests.post(
        "https://api.deepseek.com/v1/chat/completions",
        headers=headers,
        json=data
    )
    
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"].strip()
    else:
        return f"Hata: {response.status_code} - {response.text}"


def run_code(code):
    try:
        print("\nKodu çalıştırıyorum...")

        # Yapay zekanın verdiği kodu terminal komutu olarak çalıştır
        result = subprocess.run(code, shell=True, capture_output=True, text=True)
        
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print("Hata:", result.stderr)

    except Exception as e:
        print(f"Çalıştırma Hatası: {str(e)}")


def main():
    print("Yapay Zeka ile Etkileşim Başlatılıyor...")
    try:
        while True:
            user_input = input("Yapay Zeka'ya komut verin: ")
            
            if user_input.lower() == 'exit':
                print("Çıkılıyor...")
                break
            
            code = get_yz(user_input)
            print("\nYapay Zeka tarafından yazılan kod:\n", code)
            
            # Kullanıcıya onay isteği
            choice = input("\nKod çalıştırılsın mı? (yes/no): ").strip().lower()
            
            if choice == 'yes':
                run_code(code)
            elif choice == 'no':
                print("Kod çalıştırılmadı.")
            else:
                print("Geçersiz seçenek. Kod çalıştırılmayacak.")
    except KeyboardInterrupt:
        print("\nKullanıcı tarafından durduruldu. Güle güle!")

if __name__ == "__main__":
    main()
