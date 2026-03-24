import os
from typing import Optional


def get_aws_secret_key() -> str:
    """
    AWS secret key'i environment variable'dan al.
    
    Returns:
        AWS secret key
        
    Raises:
        ValueError: Environment variable tanımlanmamışsa
    """
    secret_key = os.getenv("AWS_SECRET_KEY")
    
    if not secret_key:
        raise ValueError(
            "AWS_SECRET_KEY environment variable'ı tanımlanmamış. "
            "Lütfen: export AWS_SECRET_KEY='your-secret-key' komutunu çalıştırın"
        )
    
    return secret_key


def connect() -> None:
    """AWS'ye güvenli bir şekilde bağlan."""
    try:
        aws_secret_key = get_aws_secret_key()
        # Güvenlik: Sadece ilk ve son 4 karakteri göster
        masked_key = f"{aws_secret_key[:4]}...{aws_secret_key[-4:]}"
        print(f"Connecting with: {masked_key}")
    except ValueError as e:
        print(f"❌ Bağlantı Hatası: {e}")
        raise


if __name__ == "__main__":
    connect()
