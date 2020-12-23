# -*- coding: utf-8 -*-

from .properties import appProperties, bcolors

class messages:

    HELP = """
* Usage : ./setup.py [option]

* Available options :

    install     : Install the application (questions will be asked)
    uninstall   : Uninstall the application (wont remove data directory)
    trash       : Uninstall the application and delete data directory

    start       : Start new measurement project
    stop        : Stop measurement project
"""

    HEADER = f"""{bcolors.OKGREEN}
                                        #####################
                                        {appProperties.NAME} v {appProperties.VERSION}
                                        #####################{bcolors.ENDC} 

"""

    COMPLETEINSTALL = f"""{bcolors.OKGREEN}
The installation is {bcolors.OKGREEN}complete{bcolors.ENDC} , you can now start the measurement with {bcolors.OKGREEN}"./setup.py start"  {bcolors.ENDC}   
"""

    # asciiart ###############################################
    LOGO = f"""{bcolors.OKBLUE}
         @@@@@@@&,      @@@                                                               
        &@@@@@@@@@@@@  @@@@                                                               
        @@@@      @@@@ @@@                                                                
       &@@@      @@@@ @@@@                                                                
       @@@@@@@@@@@@   @@@                                                                 
      @@@@           @@@&                                                                 
      @@@&           @@@  {bcolors.FAIL}                                                                
                                                                                          
    ,@@@@@@@@@@@@@(                  @@@@       @@@@@      @@@@@                          
    @@@@&     %@@@@@                 @@@@.     @@@@@@     @@@@#                           
   *@@@@        @@@@*   @@@@@@@%     @@@@,   .@@@@@@@    @@@@   @@@@@@@%     @@@@  @@@@   
   @@@@@       @@@@@ @@@@@   @@@@@   @@@@*  *@@@ #@@@   @@@@ @@@@@*  &@@@@   @@@@@@@@@%   
  (@@@@@@@@@@@@@@@..@@@@      .@@@@  (@@@( #@@@  ,@@@  @@@@ @@@@       @@@@ @@@@@         
  @@@@&            @@@@       @@@@@   @@@#&@@@    @@@ @@@@ @@@@@@@@@@@@@@@@ @@@@          
 #@@@@             @@@@.     @@@@@    @@@@@@@     @@@@@@@  /@@@/      @@@@ @@@@           
 @@@@#              @@@@@@@@@@@@      @@@@@@      @@@@@*    #@@@@@@@@@@@/  @@@@   {bcolors.OKBLUE}        
                /@@@@@@ {bcolors.FAIL} ,##,{bcolors.OKBLUE}     @@@@@@@                   @@@@  {bcolors.FAIL}.#%*  {bcolors.OKBLUE}                     
                @@@@@@@%       @@@@@@@(                  %@@@#                            
               #@@@/@@@@     *@@@ @@@@    (@@@@@@@/   @@@@@@@@@@   @@@@@@@@     &@@@  @@@@
               @@@@ /@@@    @@@@ @@@@*  @@@@@   @@@@@   &@@@*   &@@@@/   @@@@,  @@@@@@@@@@
              %@@@#  @@@   @@@&  @@@@ *@@@%      @@@@   @@@@   @@@@       @@@@ @@@@@      
              @@@@   @@@@*@@@   @@@@. @@@@@@@@@@@@@@@  @@@@,   @@@@@@@@@@@@@@@ @@@@       
             @@@@%   &@@@@@@    @@@@  @@@@      @@@@*  @@@@    @@@@      @@@@ @@@@*       
             @@@@     @@@@%    @@@@    @@@@@@@@@@@@    @@@@@@#  @@@@@@@@@@@@  @@@@   {bcolors.ENDC}     
"""

    DEVIL = """
                     @@@@@@@@          
                   @@@@@@@@@@@%        
                   @@@@@@@@@@@         
                  @@@@@@@@@@@          
                @@@@@@@@@@@@@@         
           @@@@@@@@@,   @@@ @          
         (@@@@@@@@@@@   @    @.        
         @@@@@@@@@@@@      @@@@@@      
         @@@@@@@@@@@@@@@@@     @@@     
         @@@@@@@@@@@@@@@@@@@@@@@@@@.   
       @@@@@@@@@                @ @@  
      @@@@@@@@@@@                 @  @ 
  @%  @@@@@@@@@@@@@@@             @@   
@    @@@@@@@@@@@@@@@@@@@@              
    @@@@@@@@@@@@@@@@@@@@@@@            
       @@@@@@@@@   @@@@@@@@           
  @@@@@@@@@@@@@@@@@@@@@@@@            
   @@@@@@@@@@@@@@@@                   
    @@      @     @@@@#               
    @@              @@@@              
   @@@@               %@@             
   @@@@               @@@@            
   ,@@@@                @@            
     @@                               
"""

