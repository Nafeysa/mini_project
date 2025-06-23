import argparse
from data_loader import load_data
from analyzer import analyze
from plotter import show_result

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--method', type=str, default='sum', help="分析方式，可选 'sum' 或 'average'")
    args = parser.parse_args()

    data = load_data()
    result = analyze(data, method=args.method)
    show_result(result)