class Resource:
    def __init__(self, resource_id, resource_type, name):
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.name = name

    def __repr__(self):
        return f"{self.resource_type}({self.resource_id}): {self.name}"


class Task:
    def __init__(self, task_id, description):
        self.task_id = task_id
        self.description = description
        self.resources = []

    def assign_resource(self, resource):
        self.resources.append(resource)

    def __repr__(self):
        return f"Task({self.task_id}): {self.description}, Resources: {self.resources}"


class ResourceManager:
    def __init__(self):
        self.resources = {}
        self.tasks = {}

    def create_resource(self, resource_id, resource_type, name):
        if resource_id not in self.resources:
            self.resources[resource_id] = Resource(resource_id, resource_type, name)
            return True
        return False

    def read_resources(self):
        return list(self.resources.values())

    def update_resource(self, resource_id, name):
        if resource_id in self.resources:
            self.resources[resource_id].name = name
            return True
        return False

    def delete_resource(self, resource_id):
        return self.resources.pop(resource_id, None) is not None

    def create_task(self, task_id, description):
        if task_id not in self.tasks:
            self.tasks[task_id] = Task(task_id, description)
            return True
        return False

    def read_tasks(self):
        return list(self.tasks.values())

    def assign_resources_to_tasks(self, task_id, resource_id):
        task = self.tasks.get(task_id)
        resource = self.resources.get(resource_id)
        if task and resource:
            task.assign_resource(resource)
            return True
        return False

    def monitor_resource_utilization(self, utilization_id):
        return {resource_id: resource for resource_id, resource in self.resources.items() if resource_id == utilization_id}


def main():
    manager = ResourceManager()
    
    while True:
        print("\nMenu:")
        print("1. Create Resource")
        print("2. Read Resources")
        print("3. Update Resource")
        print("4. Delete Resource")
        print("5. Create Task")
        print("6. Read Tasks")
        print("7. Assign Resource to Task")
        print("8. Monitor Resource Utilization")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            resource_id = int(input("Enter resource ID: "))
            resource_type = input("Enter resource type: ")
            name = input("Enter resource name: ")
            if manager.create_resource(resource_id, resource_type, name):
                print("Resource created successfully.")
            else:
                print("Resource ID already exists.")

        elif choice == '2':
            print("Resources:", manager.read_resources())

        elif choice == '3':
            resource_id = int(input("Enter resource ID to update: "))
            name = input("Enter new resource name: ")
            if manager.update_resource(resource_id, name):
                print("Resource updated successfully.")
            else:
                print("Resource ID not found.")

        elif choice == '4':
            resource_id = int(input("Enter resource ID to delete: "))
            if manager.delete_resource(resource_id):
                print("Resource deleted successfully.")
            else:
                print("Resource ID not found.")

        elif choice == '5':
            task_id = int(input("Enter task ID: "))
            description = input("Enter task description: ")
            if manager.create_task(task_id, description):
                print("Task created successfully.")
            else:
                print("Task ID already exists.")

        elif choice == '6':
            print("Tasks:", manager.read_tasks())

        elif choice == '7':
            task_id = int(input("Enter task ID to assign resource to: "))
            resource_id = int(input("Enter resource ID to assign: "))
            if manager.assign_resources_to_tasks(task_id, resource_id):
                print("Resource assigned to task successfully.")
            else:
                print("Task or resource ID not found.")

        elif choice == '8':
            utilization_id = int(input("Enter resource ID to monitor: "))
            utilization = manager.monitor_resource_utilization(utilization_id)
            print("Utilization:", utilization)

        elif choice == '9':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
