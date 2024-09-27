# Resource Management System

## Overview
The Resource Management System is a command-line application that allows users to manage resources and tasks effectively. Users can create, read, update, and delete resources and tasks, as well as assign resources to specific tasks.

## Features
- **Create Resource**: Add new resources with a unique ID, type, and name.
- **Read Resources**: List all available resources.
- **Update Resource**: Modify the name of an existing resource.
- **Delete Resource**: Remove a resource by its ID.
- **Create Task**: Add new tasks with a unique ID and description.
- **Read Tasks**: List all existing tasks along with their assigned resources.
- **Assign Resource to Task**: Link a resource to a specific task.
- **Monitor Resource Utilization**: Check the utilization of a specific resource.

## Classes
### Resource
Represents a resource with an ID, type, and name.
- `__init__(resource_id, resource_type, name)`: Initializes a new resource.
- `__repr__()`: Returns a string representation of the resource.

### Task
Represents a task with an ID, description, and assigned resources.
- `__init__(task_id, description)`: Initializes a new task.
- `assign_resource(resource)`: Assigns a resource to the task.
- `__repr__()`: Returns a string representation of the task.

### ResourceManager
Manages the resources and tasks.
- `create_resource(resource_id, resource_type, name)`: Adds a new resource.
- `read_resources()`: Returns a list of all resources.
- `update_resource(resource_id, name)`: Updates the name of a resource.
- `delete_resource(resource_id)`: Deletes a resource by its ID.
- `create_task(task_id, description)`: Adds a new task.
- `read_tasks()`: Returns a list of all tasks.
- `assign_resources_to_tasks(task_id, resource_id)`: Assigns a resource to a task.
- `monitor_resource_utilization(utilization_id)`: Monitors the utilization of a resource.

## Getting Started
### Prerequisites
- Python 3.x

### Installation
1. Clone this repository to your local machine:
   ```bash
   git clone <repository-url>
   cd resource_management_system
