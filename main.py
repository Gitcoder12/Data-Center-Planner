import json
import random
from datetime import datetime
from planner import DataCenterAreaPlanner, DataCenterRackPlanner

def load_config(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)

def get_simulated_live_temp(base_temp, rng=None):
    """Return a synthetic temperature sample; this is not live sensor telemetry."""
    rng = rng or random.Random(42)
    return round(base_temp + rng.uniform(-2.0, 2.0), 1)

if __name__ == "__main__":
    config = load_config('config.json')
    
    print("=== MACRO EVALUATION: Data Center Locations (SYNTHETIC temperature samples) ===")
    print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    area_planner = DataCenterAreaPlanner()
    rng = random.Random(42)
    
    for area in config['locations']:
        # This sample is synthetic; never label it as connected IoT telemetry.
        live_temp = get_simulated_live_temp(area['avg_temp_c'], rng)
        area['avg_temp_c'] = live_temp
        
        is_safe, score, reasons = area_planner.evaluate_area(area)
        status = "✅ APPROVED" if is_safe else "❌ REJECTED"
        
        print(f"[{status}] {area['name']} | Live Temp: {live_temp}°C | Score: {score}/110")
        for reason in reasons:
            print(f"   - {reason}")
            
    print("\n=== MICRO EVALUATION: Server Racks ===")
    rack_planner = DataCenterRackPlanner()
    for rack in config['racks']:
        is_safe, reasons = rack_planner.evaluate_rack(rack)
        status = "✅ SAFE" if is_safe else "❌ UNSAFE"
        print(f"[{status}] {rack['id']}")
        for reason in reasons:
            print(f"   - {reason}")
