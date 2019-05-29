import math

class BipedKinematics():
    def __init__(self, upper_leg_length=0.35,
                 lower_leg_length=0.33,
                 base_to_haa_length=0.15,
                 haa_to_hfe_legth=0.08,
                 leg2leg_distance=0.2):
        self.upper_leg_length = upper_leg_length
        self.lower_leg_length = lower_leg_length
        self.base_to_haa_length = base_to_haa_length
        self.haa_to_hfe_legth = haa_to_hfe_legth
        self.leg2leg_distance = leg2leg_distance

    def get_leg_joints(self, pos_x, pos_y, pos_z):
        L = (pos_x ** 2 + pos_y ** 2 + pos_z ** 2) ** 0.5
        th_L = math.atan(round(round(pos_x, 8)/-pos_z, 6))
        th3 = ((self.upper_leg_length ** 2) +
               (self.lower_leg_length ** 2) - L ** 2)
        th3 = th3/(2*self.upper_leg_length*self.lower_leg_length)
        th3 = round(th3, 8)
        th3 = math.acos(th3)-math.radians(180)

        th2 = ((self.upper_leg_length ** 2) +
               (L ** 2) - self.lower_leg_length ** 2)
        # if th2 < 0:
        th2 = th2/(2*self.upper_leg_length*L)
        th2 = round(th2, 8)
        th2 = math.acos(th2)
        th2 = th2 + th_L

        th1 = math.atan(pos_y/-pos_z)

        return th1, th2, th3

    def get_leg_pos(self, th1, th2, th3):
        inner_th3 = round(math.radians(180)+th3, 8)
        L = (self.upper_leg_length ** 2) + (self.lower_leg_length ** 2) - \
            (2*self.upper_leg_length*self.lower_leg_length*math.cos(inner_th3))

        L = L ** 0.5
        inner_th2 = ((self.upper_leg_length ** 2) +
                     (L ** 2) - self.lower_leg_length ** 2)
        inner_th2 = inner_th2/(2*self.upper_leg_length*L)
        inner_th2 = round(inner_th2, 8)
        inner_th2 = math.acos(inner_th2)

        th_L = th2 - inner_th2
        th_L = round(th_L, 8)
        L_norm = L * math.cos(th1)
        pos_y = L*math.sin(th1)

        pos_x = L * math.sin(th_L) * math.cos(th1)
        pos_z = -1*L * math.cos(th_L) * math.cos(th1)

        return pos_x, pos_y, pos_z

    def valid_check(self, pos_x, pos_y, pos_z):

        check_th1, check_th2, check_th3 = self.get_leg_joints(pos_x, pos_y, pos_z)
        check_pos_x, check_pos_y, check_pos_z = self.get_leg_pos(check_th1, check_th2, check_th3)

        if ((pos_x-check_pos_x)**2+(pos_y-check_pos_y)**2+(pos_z-check_pos_z)**2<0.01):
            return True
        else:
            return False

    def get_all_joints(self, leg_id, pos_x, pos_y, pos_z):
        # id 0 for left leg; 1 for right leg
    
        valid = self.valid_check(pos_x, pos_y, pos_z)
        if(leg_id == 0):
            th1, th2, th3 = self.get_leg_joints(pos_x - self.haa_to_hfe_legth,
                                           pos_y - self.leg2leg_distance/2,
                                           pos_z + self.base_to_haa_length)
        elif(leg_id == 1):
            th1, th2, th3 = self.get_leg_joints(pos_x - self.haa_to_hfe_legth,
                                           pos_y + self.leg2leg_distance/2,
                                           pos_z + self.base_to_haa_length)
        else:
            valid = False
        

        return valid, th1, th2, th3
    
if __name__ == '__main__':
    bi = BipedKinematics()
    # x, y, z = bi.get_leg_pos(math.radians(30), math.radians(30), -math.radians(30))
    # print(x, y, z)
    # th1, th2, th3 = bi.get_leg_joints(x, y, z)
    # print(math.degrees(th1), math.degrees(th2), math.degrees(th3))
    print(bi.get_all_joints(0,0.08,0.1,-0.63))
