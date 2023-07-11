#include "geometry.h"

void Check_Identical ( Cercle_t C1 , Cercle_t C2 )

{
  if ( C1.Radius_u8 == C2.Radius_u8 )
  puts( " Same Radius_u8 ") ;

  if  ( ( C1.Center_X_i8 == C2.Center_X_i8 ) && ( C1.Center_Y_i8 == C2.Center_Y_i8) )
  puts( " Same Center Coordiantes ") ;
}
