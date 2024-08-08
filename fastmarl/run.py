import os

import hydra
import numpy as np
from omegaconf import OmegaConf, DictConfig
import torch

import logging

OmegaConf.register_new_resolver(
    "random",
    lambda x: os.urandom(x).hex(),
)



@hydra.main(version_base=None,config_path="configs", config_name="default")
def main(cfg: DictConfig):

    print(cfg)
    logger = hydra.utils.instantiate(cfg.logger, cfg=cfg.algorithm, _recursive_=False)
    logger.info("Infoo")    

    env = hydra.utils.call(cfg.env, cfg.seed)

    # # logger.log()

    # print("\n\n\nENV =========================== \n\n\n") 
    torch.set_num_threads(1)


    if cfg.seed is not None:
        torch.manual_seed(cfg.seed)
        np.random.seed(cfg.seed)
    else:
        logger.warning("No seed has been set.")

    # print("\n\n\n SEED SET \n\n\n")
    # hydra.utils.call(cfg.algorithm, env, logger, _recursive_=False)

    # print("\n\n\n HYDRA CALL \n\n\n")

    # return logger.get_state()
    return 0

if __name__ == "__main__":

    main()
