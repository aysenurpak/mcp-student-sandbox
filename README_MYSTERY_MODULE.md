# Mystery Module - Kuadratik Denklem Çözücü

## 📋 Açıklama

`mystery_module.py` kütüphanesi, **kuadratik denklemleri çözmek** için tasarlanmış bir Python modülüdür. Standart kuadratik formülü kullanarak, verilen katsayılardan denklemin köklerini (çözümlerini) hesaplar.

### Matematiksel Temeli

Kuadratik denklem: **ax² + bx + c = 0**

Kuadratik formül:
$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

Diskriminant: **Δ = b² - 4ac**

- Δ > 0: İki farklı gerçek kök
- Δ = 0: Bir çift kök
- Δ < 0: Gerçek kök yok (None döner)

---

## 🔧 Fonksiyon: `fn_x(a, b, c)`

### Parametreler

| Parametre | Tür     | Açıklama                               |
| --------- | ------- | -------------------------------------- |
| `a`       | `float` | İkinci dereceden terim katsayısı (ax²) |
| `b`       | `float` | Birinci dereceden terim katsayısı (bx) |
| `c`       | `float` | Sabit terim katsayısı                  |

### Dönüş Değeri

- **Tuple of floats**: `(x₁, x₂)` - İki köklü tuple
- **None**: Gerçek kök yoksa (diskriminant < 0)

### Hatalar

⚠️ **Not**: Fonksiyon `a = 0` için hata üretecektir (ZeroDivisionError). Bu durumda denklem kuadratik değildir.

---

## 📚 Örnek Kullanımlar

### Örnek 1: Standart Kuadratik Denklem

```python
from mystery_module import fn_x

# Denklem: x² - 5x + 6 = 0
# Beklenen kökler: 2 ve 3
result = fn_x(1, -5, 6)
print(result)  # (3.0, 2.0)
```

### Örnek 2: Diskriminant = 0 (Çift Kök)

```python
# Denklem: x² - 4x + 4 = 0 → (x - 2)² = 0
# Beklenen kök: 2 (çift kök)
result = fn_x(1, -4, 4)
print(result)  # (2.0, 2.0)
```

### Örnek 3: Negatif Diskriminant (Gerçek Kök Yok)

```python
# Denklem: x² + 1 = 0
# Gerçek kök yok
result = fn_x(1, 0, 1)
print(result)  # None
```

### Örnek 4: Farklı Katsayılarla

```python
# Denklem: 2x² - 8x + 6 = 0
result = fn_x(2, -8, 6)
print(result)  # (3.0, 1.0)
```

---

## ✅ Test Senaryoları

```python
from mystery_module import fn_x

# Test 1: İki farklı kök
assert fn_x(1, -5, 6) == (3.0, 2.0), "Test 1 başarısız"
print("✓ Test 1 geçti")

# Test 2: Çift kök
assert fn_x(1, -4, 4) == (2.0, 2.0), "Test 2 başarısız"
print("✓ Test 2 geçti")

# Test 3: Gerçek kök yok
assert fn_x(1, 0, 1) is None, "Test 3 başarısız"
print("✓ Test 3 geçti")

# Test 4: Negatif katsayılar
result = fn_x(1, 2, 1)
assert result[0] == -1.0 and result[1] == -1.0, "Test 4 başarısız"
print("✓ Test 4 geçti")
```

---

## 🎯 Kullanım Senaryoları

- 📐 Fizik problemleri (parabol hareketi)
- 💰 İkinci dereceden maliyet analizleri
- 🔬 Bilimsel hesaplamalar
- 📊 Mühendislik uygulamaları

---

## ⚠️ Sınırlamalar ve Uyarılar

1. **a = 0 durumu**: Fonksiyon hata verir. Kontrol ekleyin:

```python
if a == 0:
    print("Bu bir kuadratik denklem değil!")
    # Doğrusal denklem: bx + c = 0 → x = -c/b
else:
    result = fn_x(a, b, c)
```

2. **Karmaşık sayılar**: Diskriminant negatifse, karmaşık kökler varsa bile None döner. Karmaşık sayı desteği için genişletilmesi gerekebilir.

3. **Sayısal Hassasiyet**: Floating-point hesaplamaları nedeniyle, çok büyük veya çok küçük sayılarla çalışırken hassasiyet kayıpları olabilir.

---

## 🔄 İyileştirme Önerileri

```python
# Geliştirilmiş versiyon (hata kontrollü)
import math
from typing import Optional, Tuple

def solve_quadratic(a: float, b: float, c: float) -> Optional[Tuple[float, float]]:
    """
    Kuadratik denklemi çöz (hata kontrollü).

    Args:
        a: ax² katsayısı
        b: bx katsayısı
        c: sabit terim

    Returns:
        (x1, x2) tuple'ı veya None

    Raises:
        ValueError: a == 0 ise
    """
    if a == 0:
        raise ValueError("a sıfır olamaz - bu bir kuadratik denklem değil!")

    discriminant = b**2 - 4*a*c

    if discriminant < 0:
        return None

    sqrt_discriminant = math.sqrt(discriminant)
    x1 = (-b + sqrt_discriminant) / (2*a)
    x2 = (-b - sqrt_discriminant) / (2*a)

    return (x1, x2)
```

---

## 📞 Destek

Sorularınız veya hataları bildirmek için lütfen bir issue açın.
