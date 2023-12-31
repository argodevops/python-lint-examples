"""
Script Name: run_simulation.py
Description: Runs a simulation command based on provided arguments and support config.

Usage: python script.py <env> <sim>

<env> - The environment argument.
<sim> - The simulation argument.

The script relies on two config files which it consults to build the simulation command.
* env.txt
* sim.txt

"""
import argparse
import logging
import os
import subprocess
import sys

import yaml


def print_usage(parser):
    parser.print_help()
    logging.error("Please provide the 'env' and 'sim' arguments.")


def check_file_exists(file_path: str):
    """check file actually exists"""
    if not os.path.isfile(file_path):
        logging.error(f"File not found: {file_path}")
        return False
    return True


def read_env_properties(env_value):
    """read and return the env properties"""
    logging.info(f"Environment: {env_value}")
    env_file = os.path.join("config", "env.yml")
    if not check_file_exists(env_file):
        return False

    with open(env_file, "r") as file:
        env_data = yaml.safe_load(file)
        for env in env_data:
            if env == env_value:
                return env_data[env_value]
    logging.info(f"Unknown environment: {env_value}")


def read_sim_properties(sim_value):
    """read and return simulation properties"""
    logging.info(f"Simulaton: {sim_value}")
    sim_file = os.path.join("config", "sim.yml")
    if not check_file_exists(sim_file):
        return False

    with open(sim_file, "r") as file:
        sim_data = yaml.safe_load(file)
        for sim in sim_data:
            if sim == sim_value:
                return sim_data[sim_value]
    logging.info(f"Unknown simulation: {sim_value}")


def write_properties_file(
    env: str, sim: str, env_props: dict, sim_props: dict, file_path: str
):
    """write properties file"""
    with open(file_path, "w") as file:
        file.write(f"\n# TEST PROPERTIES. ENV {env}, SIM {sim}\n")
        for name, value in env_props["properties"].items():
            if "$" in value:
                logging.info(f"Substituting in environment variable for {value}")
                value = os.environ.get(value[1:])
                if value is None:
                    logging.warning(f"Environment variable {value} is None")
            file.write(f"{name}={value}\n")
        for name, value in sim_props["properties"].items():
            file.write(f"{name}={value}\n")
    with open(file_path, "r") as file:
        contents = file.read()
        logging.info(contents)


### MAIN ###

# Configure logging
log_file = "output.log"
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
console = logging.StreamHandler(sys.stdout)
console.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
console.setFormatter(formatter)
logging.getLogger().addHandler(console)

# Create the argument parser
parser = argparse.ArgumentParser(
    description="Runs a simulation command based on the provided arguments "
    + "and support config"
)

# Add the mandatory arguments
parser.add_argument("env", type=str, help="Environment argument")
parser.add_argument("sim", type=str, help="Simulation argument")

# Parse the command-line arguments
args = parser.parse_args()

# Check if the arguments are empty
if not args.env or not args.sim:
    print_usage(parser)
    exit(1)

# Check if the env.yml file exists and if the provided env argument exists within it
env_props = read_env_properties(args.env)
logging.info(f"Environment properties: {env_props}")

# Check if the sim.yml file exists and if the provided sim argument exists within it
sim_props = read_sim_properties(args.sim)
logging.info("Simulation properties: {sim_props}")

if env_props is None or sim_props is None:
    logging.error("Environment or Simulation is not defined")
    exit(2)

# Building test.properties file
logging.info("Building test.properties file")
file_path = "test.properties"
write_properties_file(args.env, args.sim, env_props, sim_props, file_path)

try:
    # Execute command
    command = sim_props["command"]
    logging.info(f"Executing simulation command: {command}")
    output = subprocess.check_output(command, shell=True, universal_newlines=True)
    logging.info(f"Output: ${output}")
except subprocess.CalledProcessError as e:
    logging.error(f"Command failed with return code {e.returncode}. Error output:")
    logging.error(e.output)
