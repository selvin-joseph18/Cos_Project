from src.code.calculate_cos import calculate_cos
import sys


def main():
    angle = float(sys.argv[1])
    print calculate_cos(angle)