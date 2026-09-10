import sys
from client import TopTradingCyclesEngine

try:
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
except Exception:
    pass

def run():
    print(">>> Demonstrating Top Trading Cycles (TTC)...")
    endowments = {'Alice': 'H1', 'Bob': 'H2', 'Charlie': 'H3'}
    preferences = {
        'Alice':   ['H2', 'H1', 'H3'],
        'Bob':     ['H3', 'H2', 'H1'],
        'Charlie': ['H1', 'H3', 'H2']
    }

    ttc = TopTradingCyclesEngine(endowments, preferences)
    allocation = ttc.run()
    print(f"TTC Final Allocation: {allocation}")

    assert allocation['Alice'] == 'H2'
    assert allocation['Bob'] == 'H3'
    assert allocation['Charlie'] == 'H1'
    print("[PASS] Top Trading Cycles verified.")

if __name__ == "__main__":
    run()
