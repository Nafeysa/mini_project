def analyze(data, method='sum'):
    if method == 'sum':
        return sum(data)
    elif method == 'average':
        return sum(data) / len(data)
    else:
        raise ValueError(f"Unknown method: {method}")