class DeliveryDrone:
    def __init__(self):
        self.position = [0, 0]
        self.destination = [10, 10]
        self.battery = 100
        self.package_delivered = False
        self.obstacles_avoided = 0
        self.distance_travelled = 0

    # SENSORS
    def sensors(self):
        print("\n--- SENSOR DATA ---")
        print("GPS Position:", self.position)
        print("Altitude: 10 meters")
        print("Battery:", self.battery, "%")
        print("Camera: Scanning for obstacles...")

    # ENVIRONMENT
    def detect_obstacle(self):
        obstacles = [
            [3, 3],
            [5, 5],
            [7, 7]
        ]

        if self.position in obstacles:
            return True
        return False

    # AI DECISION MAKING
    def process(self):
        if self.battery <= 20:
            return "RETURN"

        if self.detect_obstacle():
            return "AVOID"

        if self.position == self.destination:
            return "DELIVER"

        return "MOVE"

    # ACTUATORS
    def act(self, decision):

        if decision == "MOVE":
            if self.position[0] < self.destination[0]:
                self.position[0] += 1
            elif self.position[1] < self.destination[1]:
                self.position[1] += 1

            self.battery -= 3
            self.distance_travelled += 1

            print("Actuator: Propeller motors moving drone.")
            print("Drone moved to:", self.position)

        elif decision == "AVOID":
            print("Actuator: Changing flight direction.")
            print("Obstacle avoided!")

            self.position[1] += 1
            self.battery -= 3
            self.distance_travelled += 1
            self.obstacles_avoided += 1

        elif decision == "RETURN":
            print("Battery low!")
            print("Actuator: Returning to warehouse.")

        elif decision == "DELIVER":
            print("Actuator: Package release mechanism activated.")
            self.package_delivered = True

    # PERFORMANCE MEASURE
    def performance(self):
        print("\n========== PERFORMANCE ==========")
        print("Delivery Status:",
              "SUCCESS" if self.package_delivered else "FAILED")
        print("Distance Travelled:", self.distance_travelled)
        print("Obstacles Avoided:", self.obstacles_avoided)
        print("Battery Remaining:", self.battery, "%")

    # MAIN AGENT LOOP
    def run(self):

        print("====================================")
        print("  AUTONOMOUS DELIVERY DRONE")
        print("  PEAS-BASED AI AGENT SIMULATION")
        print("====================================")

        print("\nStarting Point:", self.position)
        print("Destination:", self.destination)

        while not self.package_delivered:

            self.sensors()

            decision = self.process()
            print("AI Decision:", decision)

            self.act(decision)

            if decision == "RETURN":
                break

            if self.position == self.destination:
                self.act("DELIVER")

        self.performance()


# CREATE AND RUN THE DRONE AGENT
drone = DeliveryDrone()
drone.run()
