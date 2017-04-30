
@0xfaf0f5aa1ca0d94e;
struct Schema {
	os @0 :Text;
	openvswitch @1 :Text;
	name @2 :Text;
	ipAddr @3 :Text = "10.0.0.1";
	netmask @4 :Int64 = 24;
	gateway @5 :Text;
	masquerading @6 :Bool = true;
	dhcpEnable @7 :Bool = false;
	dhcpRangeStart @8 :Text;
	dhcpRangeStop @9 :Text;

}
