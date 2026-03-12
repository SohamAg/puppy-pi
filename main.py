#!/usr/bin/env python3

import time
import rclpy

from actions.actions import PuppyActions
from inference.inference import get_command


def main(args=None):
    rclpy.init(args=args)
    controller = PuppyActions()

    try:
        time.sleep(1.0)
        controller.stand()
        time.sleep(1.0)

        while True:
            command = get_command()

            if command == 'stand':
                controller.stand()

            elif command == 'walk':
                controller.walk_forward(speed=6.0, gait_type='Amble')

            elif command == 'left':
                controller.turn_left()

            elif command == 'right':
                controller.turn_right()

            elif command == 'stop':
                controller.stop()

            elif command == 'quit':
                controller.stop()
                break

            else:
                print("Unknown command.")

    except KeyboardInterrupt:
        controller.stop()

    finally:
        controller.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()