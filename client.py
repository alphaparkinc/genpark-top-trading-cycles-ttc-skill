class TopTradingCyclesEngine:
    """
    Shapley-Scarf Top Trading Cycles (TTC) Engine.
    Solves indivisible housing/resource allocation with initial endowments.
    Guarantees Core stability and strict Strategy-proofness.
    """
    def __init__(self, endowments, preferences):
        self.endowments = endowments
        self.house_owner = {h: a for a, h in endowments.items()}
        self.preferences = {a: list(pref) for a, pref in preferences.items()}

    def run(self):
        allocation = {}
        active_agents = set(self.endowments.keys())

        while active_agents:
            graph = {}
            for a in active_agents:
                for h in self.preferences[a]:
                    owner = self.house_owner[h]
                    if owner in active_agents:
                        graph[a] = owner
                        break

            visited = {}
            curr = list(active_agents)[0]
            path = []
            while curr not in visited:
                visited[curr] = len(path)
                path.append(curr)
                curr = graph[curr]
            cycle_start = visited[curr]
            cycle = path[cycle_start:]

            # Simultaneous cycle execution
            cycle_allocations = {}
            for a in cycle:
                for h in self.preferences[a]:
                    if self.house_owner[h] in active_agents:
                        cycle_allocations[a] = h
                        break
            for a, h in cycle_allocations.items():
                allocation[a] = h
                active_agents.remove(a)

        return allocation
