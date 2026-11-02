import json
import random
from datetime import datetime
from planner import DataCenterAreaPlanner, DataCenterRackPlanner

def load_config(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)

def get_simulated_live_temp(base_temp):
    """Simulates a live sensor reading by fluctuating the base temp slightly."""
    return round(base_temp + random.uniform(-2.0, 2.0), 1)

if __name__ == "__main__":
    config = load_config('config.json')
    
    print(f"=== MACRO EVALUATION: Data Center Locations (Live Sensor Sim) ===")
    print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    area_planner = DataCenterAreaPlanner()
    
    for area in config['locations']:
        # Simulate live data pulling from an IoT sensor
        live_temp = get_simulated_live_temp(area['avg_temp_c'])
        area['avg_temp_c'] = live_temp # Update the dictionary with the live reading
        
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
