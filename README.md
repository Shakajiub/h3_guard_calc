# h3_guard_calc
Simple python script for calculating guards in custom H3 maps. Based on the [algorithm (Heroes 3 Wiki)](https://heroes.thelazy.net//index.php/Template_Editor#Objects_and_Connections_Guards) that the official random map generator uses to place guards. For details about the logic please see the link. You still have to determine the treasure value yourself, the wiki also has all of that info easily searchable with Ctrl+F.

## Example usage
![usage_1](/usage_1.png)

1. Enter the details of the zone (Weak, Average, Strong) and monsters (Weak, Normal, Strong).
2. The script goes into a loop to start calculating the guards for your "treasures", which are any and all objects, resources, artifacts, etc.
3. When you're done, enter 'q' to quit the script.

In the example above, the value for `10,000` could be a level 5 Spell Scroll, 5 stacks of precious resources, a Town Gate, or anything else with a total value of 10,000. So for this reward, we want to place a random level `4` creature:

![usage_2](/usage_2.png)

The script tells us that the average amount of level 4 creatures would be about 40.7, so we go with something like that. We repeat until all the guards are placed, restarting the script when needed to change the initial strengths. (To determine the "treasure value" for your guards, see [the Wiki](https://heroes.thelazy.net//index.php/Template_Editor#About_Objects_and_Guards)).

### Custom multiplier

The custom multiplier you input at the start is an extra setting that the normal random map generator doesn't have. If you wish to have slightly weaker or ten times stronger guards for a specific treasure, this is the value to change. It is simply used to multiply the calculated guard value, so the default value of `1` will not differ from the official logic. `0.5`, `1.5`, `5`, or anything else is fine, completely up to you.
