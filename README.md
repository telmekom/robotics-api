# Telmekom Robotics API

## Test Entities

### Shops

* **Telmekom Dev**: 
  * **ID:** 541100015

### Robots

* **T300**: 
  * **SN:** 826084C10250007 
  * **MacAddress:** 00:D6:CB:D5:27:B3
* **CC1**: 
  * **SN:** 811114C12250003
  * **MacAddress:** 00:D6:CB:4B:17:81
* **BellaBot Pro**: 
  * **SN:** 8BR074C03050004
  * **MacAddress:** 90:03:71:42:A0:A5

## Example Snippets
### Get all Robot Positions from a Shop:
```javascript
async function fetchRobotPositions(shopId) {
  try {
    const headers = {
      'x-key': 'ABC_API_KEY_DEF' // Replace with your actual x-key
    };

    // Step 1: Fetch the list of robots
    const robotsResponse = await fetch(`https://sfscon.tmkhosting.net/robots?shop_id=${shopId}`, {
      headers
    });
    const robotsData = await robotsResponse.json();

    // Step 2: Check if "data" property exists
    if (robotsData.data && Array.isArray(robotsData.data.list)) {
      const robotList = robotsData.data.list;

      // Step 3: Loop through each robot and fetch its position
      for (const robot of robotList) {
        const sn = robot.sn;
        const positionResponse = await fetch(`https://sfscon.tmkhosting.net/robots/get-position?sn=${sn}`, {
          headers
        });
        const positionData = await positionResponse.json();

        // Step 4: Log the position data
        console.log(`Position for SN ${sn}:`, positionData);
      }
    } else {
      console.warn("No 'data.list' found in the response.", robotsData);
    }
  } catch (error) {
    console.error("Error fetching robot data:", error);
  }
}

fetchRobotPositions(541100015);
```

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
* **Robot Operations, Robot Ops**: Includes Statistics and Analysis of tasks and operations of the machines (f.ex. distance, time) - not the amount of robots or the status of them. For these informations refer to Robot Statistics / Analysis
* **Statistics**: Contrary to Analysis/Analytics it contains pure values with no charts. Can only query after the statistics are completed within one hour.
* **Analyis, Analytics**: Contrary to Statistics it focuses on charts. Can only query after the statistics are completed within one hour.

* **Delivery-Task**: Delivers to (multiple) destination point in a single trip. 
* **Cruise-Task**: "Patrol"-Mode. It circles between predefined points f.ex. for self-service drinks
* **Interactive-/Customer Attraction-Task**: Robot needs feedback / interaction
* **Customer Collection-/Solicit-Task**: The robot collects customer that then can interact with the robot
* **Pickup-/Greeter-/Lead-Task**: The robot leads customers to their tables. Then, it automatically returns to the greeting location.
* **Return-/Recovery-Task**: The robot directly returns to the pickup location or the departure location.
* **Call-Task**: Send Robot to predefined position (from App, Watch, Pager)
* **Lifting-Task**: The robot fetches from point A and delivers it to point B

* **Unit of Measurements**: Area is in m², distance in km and duration in h


## Related Links
* **Telmekom API Documentation**: https://sfscon.tmkhosting.net/docs
* **PUDU Robots**: https://www.pudurobotics.com/en/products
* **PUDU Accessories**: https://www.pudurobotics.com/en/accessory
* **PUDU Cloud API the Telmekom API is based on**: https://open.pudutech.com/