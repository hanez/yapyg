# Copyright (c) 2015 Raihan Kibria
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

"""
Controller-influenced mover
"""

import yapyg.movers
import yapyg.controls
import yapyg.entities

import yapyg.math_2d
import yapyg.debug

IDX_CONTROLLED_MOVER_CONTROLLER = yapyg.movers.IDX_MOVER_FIRST_PARAMETER
IDX_CONTROLLED_MOVER_FACTOR = yapyg.movers.IDX_MOVER_FIRST_PARAMETER + 1
IDX_CONTROLLED_MOVER_LIMITS = yapyg.movers.IDX_MOVER_FIRST_PARAMETER + 2
IDX_CONTROLLED_MOVER_SPRITES = yapyg.movers.IDX_MOVER_FIRST_PARAMETER + 3
IDX_CONTROLLED_MOVER_ROTATE = yapyg.movers.IDX_MOVER_FIRST_PARAMETER + 4
IDX_CONTROLLED_MOVER_LAST_SPRITE = yapyg.movers.IDX_MOVER_FIRST_PARAMETER + 5

def add(state, entity_name, controller, factor, limits, sprites=None, rotate=False, on_end_function=None, do_replace=False):
        """
        sprites = [idle sprite, moving sprite]
        """
        yapyg.movers.add(state, entity_name, create(entity_name, controller, factor, limits, sprites, rotate), do_replace)

def create(entity_name, controller, factor, limits, sprites=None, rotate=False):
        """
        limits = (x1, y1, x2, y2)
        """
        return ["controlled",
                run,
                entity_name,
                None,
                controller,
                factor,
                (limits[0], limits[1], limits[2], limits[3]),
                sprites,
                rotate,
                None]

def run(state, entity_name, mover, frame_time_delta, movers_to_delete):
        """
        TODO
        """
        direction = yapyg.controls.get_joystick(state)
        sprites = mover[IDX_CONTROLLED_MOVER_SPRITES]
        last_sprite = mover[IDX_CONTROLLED_MOVER_LAST_SPRITE]

        if direction[0] != 0 or direction[1] != 0:
                if sprites and (not last_sprite or last_sprite == sprites[0]):
                        mover[IDX_CONTROLLED_MOVER_LAST_SPRITE] = sprites[1]
                        yapyg.entities.set_active_sprite(state, entity_name, sprites[1])

                pos = yapyg.entities.get_pos(state, entity_name)
                factor = mover[IDX_CONTROLLED_MOVER_FACTOR]
                limits = mover[IDX_CONTROLLED_MOVER_LIMITS]
                new_x = pos[0] + (factor * (direction[0]))
                if new_x < limits[0]:
                        new_x = limits[0]
                elif new_x > limits[2]:
                        new_x = limits[2]

                new_y = pos[1] + (factor * (direction[1]))
                if new_y < limits[1]:
                        new_y = limits[1]
                elif new_y > limits[3]:
                        new_y = limits[3]

                heading = pos[2]
                if mover[IDX_CONTROLLED_MOVER_ROTATE]:
                        heading = yapyg.math_2d.get_angle((0, 0), tuple(direction))
                        heading_int = (int(heading) - 90) % 360
                        heading = (heading_int)

                # yapyg.debug.print_line(state, "control %s" % str((new_x, new_y)))
                yapyg.entities.set_pos(state, entity_name, new_x, new_y, heading)
                yapyg.collisions.run(state, entity_name)
        else:
                if sprites and (not last_sprite or last_sprite == sprites[1]):
                        mover[IDX_CONTROLLED_MOVER_LAST_SPRITE] = sprites[0]
                        yapyg.entities.set_active_sprite(state, entity_name, sprites[0])
