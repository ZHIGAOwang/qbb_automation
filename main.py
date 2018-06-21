from test_runner.qbb_test_runner import QbbTestRunner


class Main(object):

    def start_single_test(self):
        qbb = QbbTestRunner()
        qbb.run_single()

    def start_scene_test(self):
        qbb = QbbTestRunner()
        qbb.run_scene()

    def start_activity_test(self):
        qbb = QbbTestRunner()
        qbb.run_activity()


if __name__ == '__main__':
    run = Main()
    ###############  单一功能测试
    # run.start_single_test()
    ###############  场景测试
    # run.start_scene_test()
    ###############  活动测试
    run.start_activity_test()