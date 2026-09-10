import json
import sys
from client import TopTradingCyclesEngine

def handle_rpc(line):
    try:
        req = json.loads(line)
        method = req.get("method")
        params = req.get("params", {})
        rid = req.get("id")
        
        if method == "tools/list":
            tools = [
                {"name": "solve_ttc", "description": "Solve Top Trading Cycles resource allocation"}
            ]
            return json.dumps({"jsonrpc": "2.0", "id": rid, "result": {"tools": tools}})
        elif method == "tools/call":
            tname = params.get("name")
            args = params.get("arguments", {})
            if tname == "solve_ttc":
                engine = TopTradingCyclesEngine(args["endowments"], args["preferences"])
                res = engine.run()
                return json.dumps({"jsonrpc": "2.0", "id": rid, "result": {"allocation": res}})
    except Exception as e:
        return json.dumps({"jsonrpc": "2.0", "id": None, "error": {"code": -32603, "message": str(e)}})

if __name__ == "__main__":
    for line in sys.stdin:
        if line.strip():
            print(handle_rpc(line.strip()), flush=True)
