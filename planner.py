import math

class DataCenterPlanner:
    def __init__(self, thermal_limit_c=25.0, max_weight_kg=1000.0, power_capacity_kw=50.0):
        # Safety thresholds
        self.thermal_limit_c = thermal_limit_c
        self.max_weight_kg = max_weight_kg
        self.power_capacity_kw = power_capacity_kw

    def evaluate_deployment(self, rack_config):
        """
        rack_config: dict containing 'power_draw_kw', 'weight_kg', 'ambient_temp_c'
        Returns: (is_safe, reasons)
        """
        reasons = []
        is_safe = True

        # 1. Thermal Check
        if rack_config['ambient_temp_c'] > self.thermal_limit_c:
            is_safe = False
            reasons.append(f"Thermal limit exceeded: {rack_config['ambient_temp_c']}C > {self.thermal_limit_c}C")

        # 2. Structural Check
        if rack_config['weight_kg'] > self.max_weight_kg:
            is_safe = False
            reasons.append(f"Structural limit exceeded: {rack_config['weight_kg']}kg > {self.max_weight_kg}kg")

        # 3. Resource Capacity Check
        if rack_config['power_draw_kw'] > self.power_capacity_kw:
            is_safe = False
            reasons.append(f"Power capacity exceeded: {rack_config['power_draw_kw']}kW > {self.power_capacity_kw}kW")

        return is_safe, reasons

# --- Example Usage ---
if __name__ == "__main__":
    planner = DataCenterPlanner(thermal_limit_c=24.0, max_weight_kg=1500.0, power_capacity_kw=75.0)

    # A safe deployment
    safe_rack = {'power_draw_kw': 60.0, 'weight_kg': 1200.0, 'ambient_temp_c': 22.5}
    print(f"Safe Rack Evaluation: {planner.evaluate_deployment(safe_rack)}")

    # A deployment that violates all safety constraints
    unsafe_rack = {'power_draw_kw': 90.0, 'weight_kg': 1800.0, 'ambient_temp_c': 28.0}
    print(f"Unsafe Rack Evaluation: {planner.evaluate_deployment(unsafe_rack)}")
