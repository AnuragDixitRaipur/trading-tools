# Market Analysis - Anurag Dixit
# Author: Anurag Dixit

def support_resistance(prices):
    """Find basic support and resistance levels"""
    support = min(prices)
    resistance = max(prices)
    return support, resistance

def moving_average(prices, window=3):
    """Simple moving average"""
    if len(prices) < window:
        return []
    return [sum(prices[i:i+window]) / window for i in range(len(prices) - window + 1)]

if __name__ == "__main__":
    sample_prices = [100, 102, 105, 103, 108, 110, 107]
    support, resistance = support_resistance(sample_prices)
    print(f"Support: {support}, Resistance: {resistance}")
    print("3-day Moving Average:", moving_average(sample_prices))
