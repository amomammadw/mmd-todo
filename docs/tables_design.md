### BOARD
| id | title | owner (FK) |
| --- | --- | --- |

### Board Contributers
id | user_id (FK) | board_id (FK) | permission (choices)
-----------------------------------


Board Priorities
id | title | order | board_id (FK)
-----------------------------------

Board Status
id | title | order | board_id (FK) | is_completed (one true per board)
-----------------------------------

Board Category
id | title | order | board_id (FK)
-----------------------------------

Task
id | board_id (FK) | priority_id (FK) | status_id (FK) | catergory_id (FK) | title | body | media | created_time | modified_time | creator (FK) | 
-----------------------------------
