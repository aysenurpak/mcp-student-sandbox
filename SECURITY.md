# Güvenlik Kurulum Rehberi

## Ortam Değişkenlerini Yapılandırma

Bu proje AWS secret key'ini environment variable'dan okuyor. Güvenli bir şekilde kurulum yapmak için:

### 1. `.env` Dosyası Oluştur

```bash
cp .env.example .env
```

### 2. `.env` Dosyasını Düzenle

```
AWS_SECRET_KEY=your-actual-aws-secret-key
```

### 3. Kodunu Çalıştır

```bash
python secret_leak.py
```

## ⚠️ UYARILAR

- **Asla** hardcoded secret key'ler yazma
- `.env` dosyasını `.gitignore`'a ekle (zaten yapılmış)
- Secret key'leri GitHub'a commitleme
- Production'da secrets yöneticisi kullan (AWS Secrets Manager, HashiCorp Vault, vb.)

## Güvenlik İyileştirmeleri

✅ Hardcoded secret key kaldırıldı
✅ Environment variable'dan okuma eklendi
✅ Secret key maskeleme (logging'de) eklendi
✅ Hata handling eklendi
✅ .gitignore yapılandırıldı
