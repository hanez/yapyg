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
Simulate physical movement
"""

cpdef str PHYSICS_MOVER_NAME = "physics"

cpdef add(list state,
                str entity_name,
                float mass,
                float vx,
                float vy,
                float ax,
                float ay,
                float friction,
                float inelasticity,
                float vr,
                float rot_friction,
                float rot_decay,
                float stickyness,
                int do_replace=*)

cpdef list create(str entity_name,
                float mass,
                float vx,
                float vy,
                float ax,
                float ay,
                float friction,
                float inelasticity,
                float vr,
                float rot_friction,
                float rot_decay,
                float stickyness
                )

cpdef run(list state, str entity_name, list mover, float frame_time_delta, list movers_to_delete)

cpdef collision_handler(list state,
                str entity_name_1,
                str entity_name_2,
                list collision_def_1,
                list collision_def_2,
                tuple absolute_shape_1,
                tuple absolute_shape_2,
                list contact_points)

cpdef tuple get_acceleration(list mover)
cpdef set_acceleration(list mover, tuple new_acc)
cpdef tuple get_velocity(list mover)
cpdef set_velocity(list mover, tuple new_vel)
