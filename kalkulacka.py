   # Výpočet paměti vah modelu (z M1)
   parametry = 7e9          # 7 miliard parametrů
   bity = 4                 # INT4
   pamet_gb = parametry * bity / 8 / 1e9
   print(f"Paměť vah: {pamet_gb:.1f} GB"
