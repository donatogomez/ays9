
@0x9672035223fb9ad7;
struct Schema {
	name @0 :Text;
	publicSubnetCIDR @1 :Text;
	gatewayIPAddress @2 :Text;
	startIPAddress @3 :Text;
	endIPAddress @4 :Text;
	vLANID @5 :Int64 = 0;
	vdc @6 :Text;

}
