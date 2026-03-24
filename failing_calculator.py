from typing import List


def average_ratios(numbers: List[float]) -> float:
    """
    Sayıların ortalamasını hesapla (100/sayı oranı).
    
    Args:
        numbers: Sayılar listesi
        
    Returns:
        Oranların ortalaması
        
    Raises:
        ValueError: Liste boşsa veya sıfır içeriyorsa
    """
    # Girdi doğrulama
    if not numbers:
        raise ValueError("Liste boş olmamalıdır")
    
    # Sıfır değerleri kontrol et
    if 0 in numbers:
        raise ValueError(f"Sıfıra bölme hatası: Liste sıfır içeremez. Girdi: {numbers}")
    
    # Tüm değerlerin sayı olup olmadığını kontrol et
    try:
        numbers = [float(n) for n in numbers]
    except (TypeError, ValueError):
        raise ValueError("Tüm değerler sayı olmalıdır")
    
    # Oranları hesapla ve ortalamasını al
    total = sum(100 / num for num in numbers)
    return total / len(numbers)


# Test Örnekleri
if __name__ == "__main__":
    # Test 1: Normal durumda çalışma
    print("Test 1 - Normal girdi:")
    try:
        result = average_ratios([10, 5, 2])
        print(f"  Sonuç: {result:.2f}")
    except ValueError as e:
        print(f"  Hata: {e}")
    
    # Test 2: Sıfır içeren girdi
    print("\nTest 2 - Sıfır içeren girdi:")
    try:
        result = average_ratios([10, 5, 0])
        print(f"  Sonuç: {result:.2f}")
    except ValueError as e:
        print(f"  Hata: {e}")
    
    # Test 3: Boş liste
    print("\nTest 3 - Boş liste:")
    try:
        result = average_ratios([])
        print(f"  Sonuç: {result:.2f}")
    except ValueError as e:
        print(f"  Hata: {e}")
    
    # Test 4: Geçerli girdi
    print("\nTest 4 - Geçerli girdi:")
    try:
        result = average_ratios([10, 5, 20])
        print(f"  Sonuç: {result:.2f}")
    except ValueError as e:
        print(f"  Hata: {e}")
