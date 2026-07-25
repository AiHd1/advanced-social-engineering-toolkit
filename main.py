import argparse
import logging
from modules.phishing import PhishingModule
from modules.pretexting import PretextingModule

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    parser = argparse.ArgumentParser(description="Advanced Social Engineering Toolkit")
    subparsers = parser.add_subparsers(dest='module', help='Select a module')

    phishing_parser = subparsers.add_parser('phishing', help='Phishing Module')
    phishing_parser.add_argument('--template', required=True, help='Path to the phishing template')
    phishing_parser.add_argument('--target', required=True, help='Target email address')

    pretext_parser = subparsers.add_parser('pretexting', help='Pretexting Module')
    pretext_parser.add_argument('--message', required=True, help='Pretext message to send')
    pretext_parser.add_argument('--target', required=True, help='Target email address')

    args = parser.parse_args()

    try:
        if args.module == 'phishing':
            phishing_module = PhishingModule()
            phishing_module.launch_phishing_attack(args.template, args.target)
        elif args.module == 'pretexting':
            pretexting_module = PretextingModule()
            pretexting_module.send_pretext_message(args.message, args.target)
        else:
            logging.error("Invalid module selected")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()