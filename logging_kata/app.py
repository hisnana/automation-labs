import logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

def sumar(a: int, b: int) -> int:
    logging.info("Sumando %s + %s", a, b)
    return a + b
