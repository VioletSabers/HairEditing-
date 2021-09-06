class cfg:
    size = 1024

    class image:
        resize = 256


    class rec:
        size = 1024
        step = 2000
        lr = 0.05
        w_epochs = 400
        n_epochs = 400
        fs_epochs = 1000
        noise = 0.05
        noise_ramp = 0.75

    class I2SLoss:
        lamb_mse = 1e-5
        lamb_p = 1e-5
        lamb_noisemse = (1e-5,)
    
    class blend:
        lr = 0.03
        noise = 0.05
        w_epochs = 1200
        noise_ramp = 0.75
        step = 2000
        
        lamb_styleloss = 0.0002
        lamb_shapeloss = 0.00001
        lamb_classifierloss_1 = 0.0001
        lamb_classifierloss_2 = 0.000001
        lamb_mseloss = 0.005
        lamb_orientloss = 0.00001
        lamb_lpipsloss = 0.5
        
        

    class modelpath:
        segment = 'pretrain_model/inference.pth'
        styleGAN2 = 'pretrain_model/stylegan2-ffhq-config-f.pt';
    
    class styleGAN:
        size = 1024
        dimention = 512