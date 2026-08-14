import logging
import sys

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[logging.StreamHandler(sys.stderr)])

def main():
    try:
        from dify_plugin import Plugin
        from dify_plugin.config.config import DifyPluginEnv
        config = DifyPluginEnv()
        plugin = Plugin(config)
        plugin.run()
    except Exception as e:
        logging.error(f"Plugin failed to start: {e}")
        import traceback
        logging.error(traceback.format_exc())
        sys.exit(1)

if __name__ == "__main__":
    main()
