import ops
import iopc

pkg_path = ""
output_dir = ""
output_rootfs_dir = ""
squashfs_name = "kmod.squashfs"

def set_global(args):
    global pkg_path
    global output_dir 
    global output_rootfs_dir
    pkg_path = args["pkg_path"]
    output_dir = args["output_path"]
    output_rootfs_dir = ops.getEnv("LINUXKERNELMODULEROOT")

def MAIN_ENV(args):
    set_global(args)
    return False

def MAIN_EXTRACT(args):
    set_global(args)
    return True

def MAIN_PATCH(args, patch_group_name):
    set_global(args)
    for patch in iopc.get_patch_list(pkg_path, patch_group_name):
        if iopc.apply_patch(output_dir, patch):
            continue
        else:
            sys.exit(1)

    return True

def MAIN_CONFIGURE(args):
    set_global(args)

    return False

def MAIN_BUILD(args):
    set_global(args)

    iopc.make_squashfs(ops.path_join(output_rootfs_dir, ".."), output_dir, squashfs_name)
    return False

def MAIN_INSTALL(args):
    set_global(args)

    ops.copyto(ops.path_join(output_dir, squashfs_name), iopc.getOutputRootDir())
    return False

def MAIN_CLEAN_BUILD(args):
    set_global(args)

    return False

def MAIN(args):
    set_global(args)
    print "image squashfs"

