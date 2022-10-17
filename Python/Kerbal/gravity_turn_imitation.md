
# Gravity Turn Imitation

    This is an easy way to estimate heading. 
    
    Simplifies to circular orbit instead of elliptical. Only requires altitude feedback
    
## Code:

    # -*- coding: utf-8 -*-

    '''
    This is the angle needed to steadily turn the rocket up to a desired altitude

    Note: 
        This could be done more exact using feedback or estimation of the 
        semi-minor access
    '''

    import math

    class ConvertAngles:
        
        def find_degrees(self, radians):
            return radians * ( 180 / math.pi )
        
        def find_radians(self, degrees):
            return degrees * ( math.pi / 180 )

        def find_cos(self, radians):
            return math.cos(radians)

    print('Gravity turn heading\n')
    # 1) find altitude
    altitude_list = list(range(0,100001,10000))

    for alt in altitude_list:
        #alt = 50000
        desired_alt = 100000
        
        # 2) find angle (equation)
        deg_angle = 90 *  alt / desired_alt
        print('desired angle is {} degrees'.format(deg_angle))
        
        converter = ConvertAngles()
        # 3) convert to radians
        rad_angle = converter.find_radians(deg_angle)
        #print('desired angle in radians is {} radians'.format(rad_angle))
        
        # 4) get heading (cosine)
        heading = 90 * converter.find_cos(rad_angle)
        #print('desired heading is {} degrees'.format(converter.find_degrees(heading)))
        
        # 5) print heading
        print('at altitude {} the desired heading is {}'.format(alt, heading))