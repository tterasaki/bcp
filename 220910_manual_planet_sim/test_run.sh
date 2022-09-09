tele='SAT'
band=90
band_name='f090'
wafer=w25
schedule='schedule_Jupiter_oneshot.txt'
atmosphere='atmosphere.toml'
beam_file='SAT_f090_beam.p'

mpirun -np 8 /homes/tterasaki/my_soenv/repos/220909/sotodlib/workflows/toast_so_sim.py \
       `# Scan params` \
       --wafer_slots ${wafer} \
       --bands SAT_${band_name} \
       --schedule ${schedule} \
       --sim_ground.scan_rate_az "1.0 deg / s" \
       --sample_rate 37 \
       `# Simulation elements` \
       --sim_noise.enable \
       --det_pointing_azel.shared_flag_mask 0 \
       --config ${atmosphere} \
       --sim_atmosphere_coarse.enable \
       --sim_atmosphere.enable \
       --elevation_model.enable \
       `# Outputs` \
       --save_hdf5.enable \
       --mapmaker.enable \
       `# HWP parameters` \
       --sim_ground.hwp_angle 'hwp_angle'\
       --sim_ground.hwp_rpm 120\
       --weights_azel.hwp_angle 'hwp_angle'\
       `# SSO simulation` \
       --sim_sso.enable \
         --sim_sso.beam_file ${beam_file} \
       --sim_sso.sso_name "Jupiter" \
