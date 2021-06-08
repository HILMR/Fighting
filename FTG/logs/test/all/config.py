learner_config=dict(
    config_name="learner_config",
    game_number=10,
    local_data=True,
    env_name="fighting",
    learn_player_id="p0",
    ray_get_later=False,
    players=['p0'],
    learn_agent_id=['a0'],
    ray_mode="sync",
    data_config=dict(
        config_name="data_config",
        data_to_save=dict(
            player_data=['feature', 'obs', 'model_out', 'action'],
            other_data=['game_data', 'reward'],
            preprocessing_data=[],
        ),
        data_players=['p0'],
        train_data_num=10240,
        tra_len=3,
        batch_size=1024,
        data_async=False,
        data_capacity=200000,
        data_sample_mode="USWR",
        process_on_episode=False,
    ),
    trainer_config=dict(
        config_name="trainer_config",
        use_gpu=True,
        gpu_num=1,
        trainer_mode="local",
        m0=dict(
            trainer_number=1,
            trainer_name="trainer:CategoricalDQNTrainer",
            lr=0.001,
            target_model_update_iter=30,
            EPSILON=0.9,
            GAMMA=0.9,
            training_procedure=None,
            double=True,
        ),
        loss_func="MSELoss",
    ),
    eval_config=dict(
        config_name="eval_config",
        eval_game_num=10,
        total_episode_number=100,
        ray_mode="sync",
        env_name="fighting",
        players=['p0'],
        evaluator_num=1,
        eval_game_number=10,
        eval_mode="env",
    ),
    log_config=dict(
        config_name="log_config",
        log_name="default",
        time_now="2021-06-07 18:23:09",
        log_dir="logs/test",
        tb_dir="logs/tmp",
    ),
    env_config=dict(
        config_name="env_config",
    ),
    player_config=dict(
        config_name="player_config",
        players=['p0'],
        p0=dict(
            player_name="agent:SAPlayer",
            agents=['a0'],
            action_config=dict(
                action_name="greedy_action",
                epsilon=1,
                episode_count=20000,
                epsilon_enable=False,
            ),
            feature_config="tensor_feature",
        ),
        agent_config=dict(
            a0=dict(
                agent="agent:BaseAgent",
                model_id="m0",
            ),
        ),
        model_config=dict(
            m0=dict(
                model_name="model:Categorical",
                model_params=dict(
                    in_dim=144,
                    out_dim=40,
                    hidden_dim=512,
                    v_min=0,
                    v_max=8,
                    atom_size=30,
                    noisy=True,
                    dueling=True,
                ),
            ),
        ),
    ),
    player_id="p0",
    learn_model_id=['m0'],
)
league_config=dict(
    eval_config=dict(
        config_name="eval_config",
        eval_game_num=10,
        total_episode_number=100,
        ray_mode="sync",
        env_name="fighting",
        players=['p0'],
        evaluator_num=1,
        eval_game_number=10,
        eval_mode="env",
    ),
    config_name="league_config",
    eval_players=['p0'],
    eval_auto=True,
    auto_save=True,
    standings_mode=['reward', 'winrate', 'hpdiff'],
    logger=None,
    log_config=dict(
        config_name="log_config",
        log_name="default",
        time_now="2021-06-07 18:23:09",
        log_dir="logs/test",
        tb_dir="logs/tmp",
    ),
    env_config=dict(
        config_name="env_config",
    ),
    player_config=dict(
        config_name="player_config",
        players=['p0'],
        p0=dict(
            player_name="agent:SAPlayer",
            agents=['a0'],
            action_config=dict(
                action_name="greedy_action",
                epsilon=1,
                episode_count=20000,
                epsilon_enable=False,
            ),
            feature_config="tensor_feature",
        ),
        agent_config=dict(
            a0=dict(
                agent="agent:BaseAgent",
                model_id="m0",
            ),
        ),
        model_config=dict(
            m0=dict(
                model_name="model:Categorical",
                model_params=dict(
                    in_dim=144,
                    out_dim=40,
                    hidden_dim=512,
                    v_min=0,
                    v_max=8,
                    atom_size=30,
                    noisy=True,
                    dueling=True,
                ),
            ),
        ),
    ),
    env_name="fighting",
    workdir="logs/league",
)