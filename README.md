# Telmekom Robotics API

## Instructions

## Example Snippets
* **PUDU Map visualization example**: https://codesandbox.io/embed/open-map-render-kz5kf5

## FAQ and Vocabulary
* **Task**: A specific work Task for a robot. Can be scheduled or contain subtasks.
* **Command**: A modification of a Task like pausing, changing waypoints or stopping
* **Store, Shop**: Interchangable terms to represent a collection of maps, robots in a specific location. Typically has a integer id and a name
* **Map**: Represents the "geographic" information about an area of the store - identified by its name. Can include waypoints, no-go zones etc. One map is always bound to exactly one store.
* **Robot, Machine**: Interchangable terms to represents a robot - identified by a Serial Number (sn). This robot is bound to one store.
* **Vector, Position, Point**: Interchangable terms to represent a 3D-point on the map. It can be used as waypoint or as the current position of the robot.
* **QoQ**: Quarter-on-Quarter, data of the "current" quarter to the same data in the previous quarter
* **Robot Type**: Could be Industrial (T600 / T600 Underride, T300), Cleaning (MT1, CC1, SH1) or Delivery (FlashBot, BellaBot, KettyBot, PuduBot, HolaBot). X-Lab / X-Series is not yet available. A list of Robots and details can be found on the [PUDU-Website](https://www.pudurobotics.com/en/products)
* **Product Code, Machine Code**: The exact model of robot. A list of Robots and details can be found on the [PUDU-Website](https://www.pudurobotics.com/en/products)
* **Unit of Measurements**: Area is in m², distance in km and duration in h

## Related Links
* **Telmekom API Documentation**: https://URL/TO/SERVER/docs
* **PUDU Robots**: https://www.pudurobotics.com/en/products
* **PUDU Accessories**: https://www.pudurobotics.com/en/accessory
* **PUDU Cloud API the Telmekom API is based on**: https://open.pudutech.com/