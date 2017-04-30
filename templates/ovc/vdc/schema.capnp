
@0xe0283c28624942f8;
struct Schema {
	description @0 :Text;
	vdcfarm @1 :Text;
	g8client @2 :Text;
	account @3 :Text;
	location @4 :Text;
	uservdc @5 :List(Text);
	allowedVMSizes @6 :List(Int64);
	cloudspaceID @7 :Int64 = 0;
	maxMemoryCapacity @8 :Int64 = -1;
	maxCPUCapacity @9 :Int64 = -1;
	maxDiskCapacity @10 :Int64 = -1;
	maxNumPublicIP @11 :Int64 = -1;
	externalNetworkID @12 :Int64 = -1;

}
