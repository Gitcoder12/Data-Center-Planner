class DataCenterAreaPlanner:
    def __init__(self, max_temp_c=35.0, min_power_reliability=0.8, max_flood_risk=0.2):
        self.max_temp_c = max_temp_c
        self.min_power_reliability = min_power_reliability
        self.max_flood_risk = max_flood_risk

    def evaluate_area(self, area_data):
        reasons = []
        is_safe = True
        score = 100

        if area_data['flood_risk'] > self.max_flood_risk:
            is_safe = False
            reasons.append(f"CRITICAL: Flood risk too high ({area_data['flood_risk']*100}%)")
            score -= 50

        if area_data['power_reliability'] < self.min_power_reliability:
            is_safe = False
            reasons.append(f"CRITICAL: Power grid unreliable ({area_data['power_reliability']*100}%)")
            score -= 40

        if area_data['avg_temp_c'] > self.max_temp_c:
            reasons.append(f"WARNING: High ambient temperature ({area_data['avg_temp_c']}C).")
            score -= 15

        if area_data['land_cost_millions'] < 10.0:
            reasons.append(f"BONUS: Cheap land (${area_data['land_cost_millions']}M).")
            score += 10

        return is_safe, score, reasons


class DataCenterRackPlanner:
    def __init__(self, thermal_limit_c=25.0, max_weight_kg=1200.0, power_capacity_kw=80.0):
        self.thermal_limit_c = thermal_limit_c
        self.max_weight_kg = max_weight_kg
        self.power_capacity_kw = power_capacity_kw

    def evaluate_rack(self, rack_data):
        reasons = []
        is_safe = True

        if rack_data['ambient_temp_c'] > self.thermal_limit_c:
            is_safe = False
            reasons.append(f"Thermal limit exceeded: {rack_data['ambient_temp_c']}C > {self.thermal_limit_c}C")

        if rack_data['weight_kg'] > self.max_weight_kg:
            is_safe = False
            reasons.append(f"Structural limit exceeded: {rack_data['weight_kg']}kg > {self.max_weight_kg}kg")

        if rack_data['power_draw_kw'] > self.power_capacity_kw:
            is_safe = False
            reasons.append(f"Power capacity exceeded: {rack_data['power_draw_kw']}kW > {self.power_capacity_kw}kW")

        return is_safe, reasons
