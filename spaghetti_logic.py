from typing import List

# Sabitler
PRICE_INCREASE_RATE = 1.15
LOG_FILE_PATH = "log.txt"


def calculate_adjusted_prices(prices: List[float]) -> List[float]:
    """
    Fiyatlara %15 zam uygula.
    
    Args:
        prices: Orijinal fiyatlar listesi
        
    Returns:
        Zammı uygulanmış fiyatlar listesi
    """
    return [price * PRICE_INCREASE_RATE for price in prices]


def display_prices(adjusted_prices: List[float]) -> None:
    """
    Adjusted fiyatları konsola yazdır.
    
    Args:
        adjusted_prices: Zammı uygulanmış fiyatlar listesi
    """
    for price in adjusted_prices:
        formatted_price = f"Total: {price:.2f}"
        print(formatted_price)


def log_results(results: List[float], filepath: str = LOG_FILE_PATH) -> None:
    """
    İşlem sonuçlarını dosyaya kaydet.
    
    Args:
        results: Kaydedilecek sonuçlar
        filepath: Log dosyasının yolu
    """
    try:
        with open(filepath, "a") as f:
            f.write(str(results) + "\n")
    except Exception as e:
        print(f"Error occurred while writing to log file: {e}")
        
def validate_data(data: List[float]) -> None:
    """
    Veriyi doğrula: fiyatların pozitif olduğunu kontrol et.
    
    Args:
        data: Doğrulanacak fiyatlar listesi
        
    Raises:
        ValueError: Eğer herhangi bir fiyat negatifse
    """
    for price in data:
        if price < 0:
            raise ValueError(f"Invalid price detected: {price}. Prices must be non-negative.")


def process_data(data: List[float]) -> List[float]:
    """
    Veriyi işle: fiyatlara zam yap, görüntüle ve kaydet.
    
    Args:
        data: İşlenecek fiyatlar listesi
        
    Returns:
        Zammı uygulanmış fiyatlar listesi
    """
    adjusted_prices = calculate_adjusted_prices(data)
    display_prices(adjusted_prices)
    log_results(adjusted_prices)
    
    return adjusted_prices