# Boot sequence for the coop controller.
# The code is intentionally simple but safe and deterministic.

import gc
import utime

from logger import Logger

logger = Logger("BOOT")
logger.info("Initialising Smart Chicken Coop")

gc.collect()

try:
    import main
    main.run()
except Exception as exc:
    logger.error("Critical boot failure: %s" % str(exc))
    utime.sleep(5)
