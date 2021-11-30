from pathlib import Path



print(Path(__file__).resolve().parent.parent)

BASE_DIR = Path(__file__).resolve().parent
#print(BASE_DIR)

USER_DATA_PATH = BASE_DIR / "users_data"
PRODUCT_DATA_PATH = BASE_DIR / "products_data"
# print(USER_DATA_PATH)
# print(PRODUCT_DATA_PATH)