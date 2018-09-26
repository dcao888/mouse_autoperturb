import argparse
import logging
import mouse

logging.basicConfig(
                        level = logging.INFO,
                        format = "%(asctime)s:%(levelname)s: %(message)s"
                    )


def parse_arguments():
    """
    Parse mouse.perturb_autopilot() args from CLI
    """
    description = \
    """
    Simple Python Script to programatically move mouse cursor around the center of your screen at 
    fixed time increments for a predefined period of time.
    """

    parser = argparse.ArgumentParser(
                                        prog        = 'Mouse Perturbation', 
                                        description = description
                                    )

    parser.add_argument(
                            "-p", 
                            "--period",
                            type    = int, 
                            help    = "perturbation frequency period (seconds)",
                            metavar = "",
                            dest    = "period"
                        )

    parser.add_argument(
                            "-d", 
                            "--duration",
                            type    = int, 
                            help    = "total duration of all perturbation events (seconds)",
                            metavar = "",
                            dest    = "duration"
                        )
    
    return parser.parse_args()


if __name__ == "__main__":

    # get args
    args     = parse_arguments()
    period   = args.period if args.period else 5
    duration = args.duration if args.duration else 60

    # perturb mouse cursor 
    m = mouse.Mouse()

    logging.info("START: automatically perturb mouse every {}s for {}s".format(period, duration))

    m.perturb_autopilot(
                            period   = period, 
                            duration = duration
                        )

    logging.info("FINISH: mouse autopilot OFF!")