#!/usr/bin/env python3

from protocol.srv import MotionResultCmd
import rclpy
from rclpy.node import Node


class CyberdogRemoteClientAsync(Node):

    def __init__(self):
        super().__init__('cyberdog_remote_client_async')
        self.cli = self.create_client(MotionResultCmd, '/mi_desktop_48_b0_2d_5f_ad_df/motion_result_cmd')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.get_logger().info('service available now')
        self.req = MotionResultCmd.Request()

    def send_request(self, motion_id):
        self.req.motion_id = motion_id
        self.req.cmd_source = 0
        self.future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()


def main():
    motion_id = 111

    rclpy.init()
    minimal_client = CyberdogRemoteClientAsync()
    response = minimal_client.send_request(motion_id)
    minimal_client.get_logger().info(
        'Response of Cyberdog: %d' %
        (response.result))

    minimal_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()